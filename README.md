# Parcial2ISO2
Nicolas Alberto Cuellar Castrellon 2220906

El motivos de mis decisiones para la elección de los patrones y el antipatrón así como la
arquitectura, se basa en:

1. Patrón Singleton – DatabaseConnection

    Escogido para ilustrar cómo garantizar que una clase tenga una única instancia y proporcionar un punto global de acceso.

    Es especialmente útil para simular conexiones a bases de datos donde múltiples instancias podrían provocar conflictos o sobrecarga.

2. Patrón Factory Method – ProductFactory

    Elegido para abstraer la lógica de creación de objetos (Laptop, Smartphone, etc.), permitiendo mayor flexibilidad y escalabilidad en el sistema.

    Ayuda a mantener un bajo acoplamiento entre la lógica del negocio y las clases concretas.

3. Antipatrón: God Object – StoreManager

    Se implementó a propósito para demostrar un ejemplo de mala práctica.

    StoreManager centraliza demasiadas responsabilidades: control de inventario, generación de reportes, conexión a base de datos, lógica de negocios e incluso simulación de servicios.

    Esto viola el principio de responsabilidad única (SRP), lo que dificulta el mantenimiento, la prueba y la evolución del sistema.

    Sirve como advertencia visual y funcional de cómo no estructurar una clase principal en sistemas reales.

4. Arquitectura Monolítica

    Se eligió este enfoque arquitectónico por su simplicidad y por ser común en proyectos pequeños o de inicio.

    Todo el sistema está contenido dentro de un único bloque funcional donde los módulos están estrechamente acoplados y comparten la misma base de código.

    Esto facilita su desarrollo inicial, pero demuestra las limitaciones para escalar, desacoplar o mantener un sistema a largo plazo.

Todas estas decisiones se hicieron tomando en cuenta las exposiciones y archivos presentes en la carpeta "Material de clase" compartida en Drive.

    Representa un enfoque "todo en uno" que refuerza el objetivo pedagógico del proyecto: observar claramente el impacto de las decisiones arquitectónicas.

