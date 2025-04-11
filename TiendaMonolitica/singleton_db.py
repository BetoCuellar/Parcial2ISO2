class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Conectando a la base de datos...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def query(self, sql):
        print(f"Ejecutando consulta: {sql}")
