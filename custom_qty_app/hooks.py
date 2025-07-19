doc_events = {
    "Sales Order": {
        "before_save": "custom_qty_app.sales_order_custom.set_available_qty"
    }
}
