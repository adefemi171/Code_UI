CREATE TABLE Product(pid INT NOT NULL, 
                     bid VARCHAR(25) NOT NULL, 
                     pname VARCHAR(30) NOT NULL, 
                     unit_price REAL NOT NULL,
                     sid INT NOT NULL,
                     cid INT NOT NULL,
                     CONSTRAINT PK_Product PRIMARY KEY(pid),
                     FOREIGN KEY(sid) REFERENCES Store(sid),
                     FOREIGN KEY(cid) REFERENCES Category(cid));

CREATE TABLE Store(sid INT NOT NULL, 
                    store_name VARCHAR(30) NOT NULL,
                    CONSTRAINT PK_Store PRIMARY KEY(sid));

CREATE TABLE Category(cid INT NOT NULL, 
                     cname VARCHAR(30) NOT NULL,
                     subc_name VARCHAR(30) NOT NULL,
                     CONSTRAINT PK_Category PRIMARY KEY(cid));

CREATE TABLE Supplier(supplier_id INT NOT NULL, 
                     supplier_name VARCHAR(30) NOT NULL, 
                     sid INT NOT NULL,
                     pid INT NOT NULL,
                     CONSTRAINT PK_Supplier PRIMARY KEY(supplier_id),
                     FOREIGN KEY(sid) REFERENCES Store(sid),
                     FOREIGN KEY(pid) REFERENCES Product(pid)); 

CREATE TABLE Sale(sales_id INT NOT NULL, 
                    date DATE NOT NULL,
                    quantity INT NOT NULL,
                    sid INT NOT NULL,
                    pid INT NOT NULL,
                    CONSTRAINT PK_Sales PRIMARY KEY(sales_id),
                    FOREIGN KEY(sid) REFERENCES Store(sid),
                    FOREIGN KEY(pid) REFERENCES Product(pid));


INSERT INTO Sale(sales_id, date, quantity, sid, pid) VALUES(1, '2021-02-01', 3, 2, 1),
                                                                (2, '2021-02-12', 6, 4, 3),
                                                                (3, '2021-03-06', 5, 3, 4),
                                                                (4, '2021-04-07', 1, 1, 5),
                                                                (5, '2021-04-14', 4, 5, 2);


INSERT INTO Product(pid, bid, pname, unit_price, sid, cid) VALUES(1, 'A-0010-Z', 'Milo', 2999.99, 1, 2),
                                                                (2, 'A-0030-Z', 'Mcvities Biscuit', 399.99, 4, 4),
                                                                (3, 'A-0020-Z', 'Dangote Sugar', 249.99, 5, 3),
                                                                (4, 'A-0015-Z', "Dano Milk", 2479.89, 3, 5),
                                                                (5, 'A-0025-Z', 'Bod Man Spray', 6270.55, 2, 1);
INSERT INTO Store(sid, store_name) VALUES(1, 'Dugbe Market'),
                                         (2, 'Dugbe Railway'),
                                         (3, 'Dugbe Onireke'),
                                         (4, 'Dugbe Ogunpa'),
                                         (5, 'Dugbe Cocoa House');

INSERT INTO Category(cid, cname, subc_name) VALUES(2, 'Beverages', 'Chocolate'),
                                                  (1, 'Personal Care', 'Body Spray'),
                                                  (3, 'Beverages', 'Dry'),
                                                  (4, 'Cookies', 'Biscuit'),
                                                  (5, 'Beverages', 'Dairy');

INSERT INTO Supplier(supplier_id, supplier_name, sid, pid) VALUES(1, 'Exclusive Beverages', 2, 1),
                                                                (2, 'Exclusive Beverages', 4, 3),
                                                                (3, 'Exclusive Beverages', 3, 4),
                                                                (4, 'Shokem Body Treatment', 1, 5),
                                                                (5, 'Oreos Snacks (Nasco)', 5, 2);


Where pid == Product ID
      bid == Barcode ID
      pname == Product Name
      sid == Store ID
      cid == Category ID
      cname == Category Name
      subc_name == Subcategory Name