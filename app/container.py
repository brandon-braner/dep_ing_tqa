from lagom.integrations.fast_api import FastApiIntegration
from lagom import Container

from app.modules.payments.repository import PaymentRepository

container = Container()
deps = FastApiIntegration(container)


container[PaymentRepository] = PaymentRepository