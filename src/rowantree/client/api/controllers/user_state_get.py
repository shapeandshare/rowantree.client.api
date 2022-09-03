from typing import Any, Tuple

from starlette import status
from starlette.exceptions import HTTPException

from ..contracts.dto.user_notification import UserNotification
from ..contracts.dto.user_state import UserState
from ..db.incorrect_row_count_error import IncorrectRowCountError
from .abstract_controller import AbstractController


class UserStateGetController(AbstractController):
    def execute(self, user_guid: str) -> UserState:
        # TODO: fill in once other response structures have been verified and defined

        # User Game State
        try:
            active: bool = self.dao.user_active_state_get(user_guid=user_guid)
        except IncorrectRowCountError as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") from error

        # User Stores (Inventory)
        stores: Any = self.dao.user_stores_by_guid_get(user_guid=user_guid)

        # User Income
        incomes: Any = self.dao.user_income_by_guid_get(user_guid=user_guid)

        # Features
        features: list[Tuple[str]] = self.dao.user_features_get(user_guid=user_guid)

        # Population
        population: int = self.dao.user_population_by_guid_get(user_guid=user_guid)

        # Active Feature
        active_features: list[Tuple[str]] = self.dao.user_active_feature_get(user_guid=user_guid)

        # Active Feature Details
        active_features_details: list[Tuple[str, Any]] = self.dao.user_active_feature_state_details_get(
            user_guid=user_guid
        )

        # Merchants
        merchants: list[Tuple[str]] = self.dao.user_merchant_transforms_get(user_guid=user_guid)

        # Notifications
        notifications: list[UserNotification] = self.dao.user_notifications_get(user_guid=user_guid)

        user_state: UserState = UserState(
            active=active,
            stores=stores,
            incomes=incomes,
            features=features,
            active_features=active_features,
            active_features_details=active_features_details,
            population=population,
            merchants=merchants,
            notifications=notifications,
        )
        return user_state
