class Carts:
    def __init__(self, request):
        self.session =request.session

        carts=self.session.get('session_key')
        if 'session_key' not in request.session:
            carts=self.session['session_key']={}

        self.carts = carts

    def add(self, product):
        product_id  = str(product.id)

        if product_id in self.carts:
            pass

        else:
            self.carts[product_id] = {'price':str(product.price)}


        self.session.modified = True

        


    def __len__(self):
        return len(self.carts)