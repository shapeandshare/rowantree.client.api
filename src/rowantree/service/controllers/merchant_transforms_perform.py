from rowantree.service.sdk.contracts.requests.merchant_transform import MerchantTransformRequest

from .abstract_controller import AbstractController


class MerchantTransformPerformController(AbstractController):
    def execute(self, user_guid: str, request: MerchantTransformRequest) -> None:
        self.dao.merchant_transform_perform(user_guid=user_guid, store_name=request.store_name)
