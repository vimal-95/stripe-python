from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class SubscriptionItem(CreateableAPIResource, DeletableAPIResource,
                       UpdateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'subscription_item'

    @classmethod
    def class_name(cls):
        return 'subscription_item'
