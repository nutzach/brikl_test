CREATE TABLE Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    available_date DATE NOT NULL,
    stock_quantity INTEGER NOT NULL,
    images TEXT NOT NULL,
    category TEXT NOT NULL,
    is_promotional BOOLEAN NOT NULL
);

CREATE TABLE Catalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE CatalogProduct (
    catalog_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (catalog_id) REFERENCES Catalog (id),
    FOREIGN KEY (product_id) REFERENCES Product (id)
);

CREATE TABLE Storefront (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE StorefrontCatalog (
    storefront_id INTEGER NOT NULL,
    catalog_id INTEGER NOT NULL,
    FOREIGN KEY (storefront_id) REFERENCES Storefront (id),
    FOREIGN KEY (catalog_id) REFERENCES Catalog (id)
);

CREATE TABLE StorefrontProduct (
    storefront_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (storefront_id) REFERENCES Storefront (id),
    FOREIGN KEY (product_id) REFERENCES Product (id)
);

CREATE TABLE MicroStore (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE Inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE InventoryProduct (
    inventory_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (inventory_id) REFERENCES Inventory (id),
    FOREIGN KEY (product_id) REFERENCES Product (id)
);