# -*- coding: utf-8 -*-

import warnings

from . import models


warnings.warn(
    "djstripe.stripe_objects is a deprecated module, please use djstripe.models",
    DeprecationWarning
)

StripeObject = models.StripeObject
StripeCharge = models.Charge
StripeCustomer = models.Customer
StripeEvent = models.Event
StripePayout = models.Payout
StripeCard = models.Card
StripeCoupon = models.Coupon
StripeInvoice = models.Invoice
StripePlan = models.Plan
StripeSubscription = models.Subscription
StripeAccount = models.Account
StripeTransfer = models.Transfer
