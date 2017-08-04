from datetime import datetime, timedelta

from buda.entities.subscription_cancelled_pb2 import SubscriptionCancelled
from buda.entities.subscription_created_pb2 import SubscriptionCreated
from buda.entities.subscription_period_updated_pb2 import SubscriptionPeriodUpdated
from buda.entities.subscription_status_pb2 import SubscriptionStatus
from buda.entities.payment_terms_pb2 import PaymentTerms
from buda.entities.payment_schedule_pb2 import PaymentSchedule
from buda.entities.payment_type_pb2 import PaymentType

from client.utils import *


def make_test_subscription_created():
    sub_id =new_uuid()
    user_id=new_uuid()
    plan_id = new_uuid()
    plan_name = 'NewAwesomePlan'
    gateway_customer_id = '123456789'

    event = SubscriptionCreated(
        id=new_uuid(),
        user_id=user_id,
        subscription=SubscriptionCreated.Subscription(
            id=sub_id,
            status = SubscriptionStatus.Value('ACTIVE'),
            plan_id = plan_id,
            plan_name = plan_name,
            gateway_customer_id = gateway_customer_id,
            payment_terms = PaymentTerms.Value('NET_60'),
            payment_schedule = PaymentSchedule.Value('QUARTERLY'),
            term_value = 100000.57,
        ),
        payment = SubscriptionCreated.Payment(
            id=new_uuid(),
            payment_type = PaymentType.Value('BANK'),
            payment_amount = 999.99,
            payment_currency = 'USD'
        )
    )

    event.created_at.GetCurrentTime()
    event.subscription.initial_period_start.GetCurrentTime()
    event.subscription.initial_period_end.FromDatetime(datetime.now() + timedelta(60))

    return event

def make_test_subscription_cancelled(sub_id=new_uuid(), user_id=new_uuid()):
    event = SubscriptionCancelled(
        id=new_uuid(),
        user_id=user_id,
        subscription_id=sub_id
    )

    event.created_at.GetCurrentTime()

    return event
def make_test_subscription_period_updated(sub_id=new_uuid(), user_id=new_uuid()):
    event = SubscriptionPeriodUpdated(
        id=new_uuid(),
        user_id=user_id,
        subscription=SubscriptionPeriodUpdated.Subscription(
            id=sub_id,
            status = SubscriptionStatus.Value('ACTIVE')
        ),
        payment = SubscriptionPeriodUpdated.Payment(
            id=new_uuid(),
            payment_type = PaymentType.Value('BANK'),
            payment_amount = 999.99,
            payment_currency = 'USD'
        )
    )

    event.created_at.GetCurrentTime()
    event.subscription.new_period_start.GetCurrentTime()
    event.subscription.new_period_end.FromDatetime(datetime.now() + timedelta(60))

    return event

def run_test(stub):
    subs = send_test_events(make_test_subscription_created,
        stub.CollectSubscriptionCreated)

    maker = lambda s: make_test_subscription_period_updated(s.subscription.id, s.user_id)

    send_test_events_from_list(subs, maker,
        stub.CollectSubscriptionPeriodUpdated)

    maker = lambda s: make_test_subscription_cancelled(s.subscription.id, s.user_id)

    send_test_events_from_list(subs, maker,
        stub.CollectSubscriptionCancelled)
