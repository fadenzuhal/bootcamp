class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self,product,quantity):
        if product.update_stock(quantity):
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product':product, 'quantity': quantity}

    def remove_product(self,product_name):
        if product_name in self.items:
            del self.items[product_name]

    def display_cart(self):
        for item in self.items.values():
            print(f"{item['product'].name} - {item['quantity']} adet - {item['product'].price * item['quantity']} TL")
    
    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values)
class Order:
       def __init__(self,customer,cart):
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_total()
    
       def place_order(self):
        if self.total_amount > 0:
            print(f"\nSiparişiniz başarıyla oluşturuldu: ")
            print(self.customer)
            print("\nSipariş detayları:")
            self.cart.display_cart()
            print(f"Toplam Tutar: {self.total_amount} TL")
        else:
            print("\n Sepet boş, siparişiniz oluşturulamadı!")

class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self,quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
    
    def __str__(self):
        return f"{self.name} - {self.price} TL (Stok: {self.stock})"
      
""" sınıfı bu şekilde yaptım"""
class main(Cart,Order,Product): #miras aldım
    
   def __init__(self):
      self.cart = Cart()
      self.products = []  

      self.product1 = Product("ll", 300, 19)
      self.product2 = Product("kk", 1230, 8)
      self.products.append(self.product1)
      self.products.append(self.product2)
        
      
      self.yap()

def yap(self):
      
      
      while True:
       print("islem seçiniz:")
       print("1. Ürün ekle")
       print("2. Ürün çıkar")
       print("3. Sepeti görüntüle")
       print("4. Siparişi Tamamla")
       print("5. Çıkış")
       i=int(input("islem seciniz:"))
 
       if i==1:
            ad=str(input("ad giriniz"))
            quantity = int(input("Adet giriniz: "))
       self. Cart.add_product(self.products[self.ad],quantity)
       if i==2:
            ad=str(input("ad giriniz"))
            
            self.Cart.remove_product(self.products[self.ad])
       if i==3:
            print(Cart.display_cart)
       if i==4:
            print(Order.place_order)

       if i==5:
          print("çıkış yapılıyor.")
          break
      
      
     
          




         


         

    