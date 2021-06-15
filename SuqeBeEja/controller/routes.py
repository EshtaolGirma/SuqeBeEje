from flask import request
from flask_restplus import Resource
from SuqeBeEja import api
from SuqeBeEja.model.models import seller_model_templet, customer_model_templet, product_model_templet
from SuqeBeEja.service.authentication import authenticationfunction
from SuqeBeEja.service.registration import createSellerAccountFun, createCustomerAccountFun
from SuqeBeEja.service.updateAccount import updateCustomerFun, updateSellerFun
from SuqeBeEja.service.deleteAccount import deleteCustomerFun, deleteSellerFun
from SuqeBeEja.service.displayAccount import displayCustomerAccount, displaySalesPersonAccount
from SuqeBeEja.service.manipulateItems import addNewItem, updateItem, deleteItem
from SuqeBeEja.service.displayItems import displayFeaturedItems, displayItemsByDepartment, displayItemsBySubDepartment, displayItemsByName
from SuqeBeEja.service.manipulateCart import displayCartContent, addItemToCart, editItemOnCart, deleteItemFromCart
from SuqeBeEja.service.purchase import payout, purchaseHistroy
from SuqeBeEja.service.salesStatistics import sellerStatistics


seller_model = api.model(
    'Seller', seller_model_templet
)
customer_model = api.model(
    'Customer', customer_model_templet
)

product_model = api.model("Items", product_model_templet)


api_section_account = api.namespace(
    'Account', description='Create and display user account')


@api_section_account.route('/customer/')
class createCustomerAccount(Resource):
    @api.expect(customer_model)
    def post(self):
        '''
        create customer profile
        '''
        return createCustomerAccountFun(request.json)


@api_section_account.route('/salesperson/')
class createSellerAccount(Resource):
    @api.expect(seller_model)
    def post(self):
        '''
        create salesperson profile
        '''
        return createSellerAccountFun(request.json)


@api_section_account.route('/display/<int:user_type>/<int:user_id>/')
class DisplayProfile(Resource):

    def get(self, user_type, user_id):
        '''
        View Profile
        '''
        if user_type == 1:
            return displaySalesPersonAccount(user_id)
        elif user_type == 2:
            return displayCustomerAccount(user_id)


api_section_authentication = api.namespace(
    'Authentication', description="login logout")


@api_section_authentication.route('/<string:email>/<string:password>')
class authentication(Resource):
    def post(self, email, password):
        '''
        login to the system
        '''
        return authenticationfunction(email, password)


api_section_salesperson = api.namespace(
    'Salesperson', description='Manipulate sales person info')


@api_section_salesperson.route('/<string:seller_id>/items/')
class Salesperson(Resource):
    def get(self, seller_id):
        '''
        view Pervious sales Statistics
        '''
        return sellerStatistics(seller_id)

    @api.expect(product_model)
    def post(self, seller_id):
        '''
        Add new item for sale
        '''
        return addNewItem(request.json, seller_id)


@api_section_salesperson.route('/<int:seller_id>/items/<int:item_id>/')
class Salesperson(Resource):
    @api.expect(product_model)
    def put(self, seller_id, item_id):
        '''
        Edit item details
        '''
        return updateItem(request.json, seller_id, item_id)

    def delete(self, seller_id, item_id):
        '''
        Delete item form sale
        '''
        return deleteItem(seller_id, item_id)


@api_section_salesperson.route('/account/<int:salesperson_id>/')
class SalespersonAccount(Resource):
    @api.expect(seller_model)
    def put(self, salesperson_id):
        '''
        edit Salesperson profile
        '''
        return updateSellerFun(request.json, salesperson_id)

    def delete(self, salesperson_id):
        '''
        remove Salesperson profile
        '''
        return deleteSellerFun(salesperson_id)


api_section_customer = api.namespace(
    'Customer', description='Manipulate customer info')


@api_section_customer.route('/PreviousPurchase/<int:customer_id>/')
class PreviousPurchase(Resource):
    def get(self, customer_id):
        '''
        View Previous Purchase
        '''
        return purchaseHistroy(customer_id)


@api_section_customer.route('/Checkout/<int:customer_id>/')
class checkout(Resource):
    def post(self, customer_id):
        '''
        checkout what on the cart
        '''
        return payout(customer_id)


@api_section_customer.route('/account/<int:customer_id>/')
class customerAccount(Resource):
    @api.expect(customer_model)
    def put(self, customer_id):
        '''
        edit customer profile
        '''
        return updateCustomerFun(request.json, customer_id)

    def delete(self, customer_id):
        '''
        remove customer profile
        '''
        return deleteCustomerFun(customer_id)


api_section_cart = api.namespace(
    'Cart', description='Manipulate customer cart')


@api_section_cart.route('/<int:customer_id>/<int:product_id>/<int:amount>/')
class Cart(Resource):
    def post(self, customer_id, product_id, amount):
        '''
        add new item to your cart
        '''
        return addItemToCart(customer_id, product_id, amount)

    def put(self, customer_id, product_id, amount):
        '''
        edit item on your cart
        '''
        return editItemOnCart(customer_id, product_id, amount)


@api_section_cart.route('/<int:customer_id>/<int:product_id>/')
class deleteCart(Resource):

    def delete(self, customer_id, product_id):
        '''
        remove item from your cart
        '''
        return deleteItemFromCart(customer_id, product_id)


@api_section_cart.route('/<int:customer_id>/')
class DisplayCart(Resource):
    def get(self, customer_id):
        '''
        view what's on your cart
        '''
        return displayCartContent(customer_id)


api_section_search_items = api.namespace(
    'Search Items', description='Search for items in our store')


@api_section_search_items.route('/api/featured/')
class Featured(Resource):
    def get(self):
        '''
        featured items
        '''
        return displayFeaturedItems()


@api_section_search_items.route('/dep/<string:department_name>/')
class SearchItemsByDep(Resource):
    def get(self, department_name):
        '''
        search by Department 
        '''

        return displayItemsByDepartment(department_name)


@api_section_search_items.route('/subdep/<string:sub_department_name>/')
class SearchItemsBySubDep(Resource):
    def get(self, sub_department_name):
        '''
        search by sub Department 
        '''
        return displayItemsBySubDepartment(sub_department_name)


@api_section_search_items.route('/item/<string:product_name>/')
class SearchItemsDirectly(Resource):
    def get(self, product_name):
        '''
        search Directly
        '''
        return displayItemsByName(product_name)
