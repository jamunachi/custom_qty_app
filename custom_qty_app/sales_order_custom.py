import frappe
from frappe.utils import now

def set_available_qty(doc, method):
    """
    Fills custom_available_qty for each item row based on actual_qty - reserved_stock,
    using custom Bin filters. Includes logging and error handling.
    """
    try:
        if not doc.custom_from_warehouse:
            frappe.logger().info(f"[{now()}] Skipping qty update: No 'custom_from_warehouse' on Sales Order {doc.name}")
            return

        for item in doc.items:
            if not item.item_code:
                continue

            try:
                bins = frappe.get_all(
                    "Bin",
                    filters={
                        "item_code": item.item_code,
                        "custom_warehouse_area": doc.custom_from_warehouse,
                        "custom_type_of_warehouse": doc.custom_type_of_warehouse
                    },
                    fields=["actual_qty", "reserved_stock"]
                )

                if bins:
                    total_qty = sum(b["actual_qty"] - b["reserved_stock"] for b in bins)
                    item.custom_available_qty = total_qty
                else:
                    item.custom_available_qty = 0

                frappe.logger().info(
                    f"[{now()}] Sales Order {doc.name} | Item {item.item_code} → Qty: {item.custom_available_qty}"
                )

            except Exception as item_err:
                frappe.logger().error(
                    f"[{now()}] Error processing item {item.item_code} on Sales Order {doc.name}: {str(item_err)}"
                )
                item.custom_available_qty = 0  # fallback to 0 if there's an error

    except Exception as err:
        # Critical failure - log for devs
        frappe.logger().error(
            f"[{now()}] Failed to update available qty on Sales Order {doc.name}: {str(err)}"
        )
        # Optionally show a message to user:
        frappe.msgprint("Something went wrong while calculating available stock. Please contact support.")
