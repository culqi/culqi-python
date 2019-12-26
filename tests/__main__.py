import unittest

from .test_version import VersionTest
from .test_client import ClientTest

from .test_token import TokenTest
from .test_card import CardTest
from .test_charge import ChargeTest
from .test_customer import CustomerTest
from .test_event import EventTest
from .test_iin import IinTest
from .test_order import OrderTest
from .test_plan import PlanTest
from .test_refund import RefundTest
from .test_suscription import SuscriptionTest
from .test_transfer import TransferTest


if __name__ == "__main__":
    unittest.main()
