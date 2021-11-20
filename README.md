# payping

payping is a Python library for using web services (www.payping.ir)

[documentation](https://docs.payping.ir/)

پی پینگ یک کتابخانه پایتون برای استفاده از خدمات پرداخت وب سروریس پی پینگ دات ایر است

[مستند ها سایت](https://docs.payping.ir/)

## Installation

Use the package manager [pip](https://pypi.org/project/payping/) to install payping.

```bash
pip install payping
```

## Usage

دریافت توکن

GET Token

```python
from payping.authentication import Bearer

# returns header with token
Bearer(token='')

```

ساخت کد پرداخت

make payment code

```python
from payping.payment import make_payment_code

# returns code
make_payment_code(header='', amount='', returnUrl='')

```

ادرس صفحه پرداخت

GET url payment

```python
from payping.payment import get_url_payment

# returns url
get_url_payment(code='')

```

ادرس صفحه پرداخت

GET url payment

```python
from payping.payment import get_url_payment

# returns url
get_url_payment(code='')

```

ادرس صفحه پرداخت

GET url payment

```python
from payping.payment import verify_payment

# returns response amount cardNumber cardHashPan
verify_payment(header='', refid='', amount='')

```

## example
[نمونه کد](https://github.com/rahimaee/example_payping.git) برای استفاده پی پینک

example code payping [github](https://github.com/rahimaee/example_payping.git)

## License

[MIT](https://github.com/rahimaee/smsir/blob/main/LICENSE)