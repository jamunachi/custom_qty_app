# Custom Qty App

This is a custom Frappe app for modifying quantity behavior in Sales Orders.

## Features

- Custom logic for Sales Order quantities
- Easily integratable with existing ERPNext setups

## Installation

1. Get the app:
   ```bash
   bench get-app custom_qty_app /path/to/custom_qty_app
   ```

2. Install it on your site:
   ```bash
   bench --site your-site-name install-app custom_qty_app
   ```

## File Structure

```
custom_qty_app/
├── __init__.py
├── hooks.py
└── sales_order_custom.py
```

## License

MIT – see [LICENSE](LICENSE) for details.