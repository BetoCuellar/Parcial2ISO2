from store_manager import StoreManager

def main():
    tienda = StoreManager()

    tienda.add_product("laptop", "Dell XPS", 1200)
    tienda.add_product("smartphone", "iPhone 14", 999)

    tienda.list_products()

    tienda.update_price("Dell XPS", 1100)
    tienda.delete_product("iPhone 14")

    tienda.list_products()

    # Funciones adicionales de God Object
    tienda.generate_report()
    tienda.send_emails()
    tienda.manage_inventory()

if __name__ == "__main__":
    main()
