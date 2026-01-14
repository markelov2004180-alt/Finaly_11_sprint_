import configuration
import data 
import requests

def post_new_orders ():
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                        json = data.order_body)
response_post = post_new_orders()
response_data = response_post.json()


def get_track_orders(track):

    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_NUMBER,
                        params={"t": track})
