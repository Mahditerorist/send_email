# send_email

`send_email` یک کتابخانه ساده برای ارسال ایمیل‌ها از طریق یک API است.

## نصب

برای نصب این کتابخانه، می‌توانید از `pip` استفاده کنید:

```bash
pip install git+https://github.com/Mahditerorist/send_email.git
```

استفاده
در زیر یک مثال ساده برای استفاده از این کتابخانه آورده شده است:

```python
Copy code
from send_email import Email

# تنظیمات ایمیل
setup = Email(
    To='mahdiahmadi.1208@gmail.com',
    text='hi',
    Title='Codern',
    Token='d9206bbfc8ec95fbf2c2c07f1f295014',
    Input='iran'
)

# ارسال ایمیل
print(setup.Send())
```
توضیحات پارامترها
To: آدرس ایمیل گیرنده.
text: متن ایمیل.
Title: عنوان ایمیل.
Token: توکن احراز هویت برای استفاده از API.
Input: نوع ورودی (مثلاً 'info', 'app', 'Login', 'support').
API مورد استفاده
این کتابخانه از یک API برای ارسال ایمیل‌ها استفاده می‌کند. لطفاً مطمئن شوید که توکن احراز هویت صحیح را وارد کرده‌اید.

مشارکت
اگر مایل به مشارکت در توسعه این کتابخانه هستید، می‌توانید مخزن را فورک کرده و تغییرات خود را از طریق Pull Request ارسال کنید.

مجوز
این پروژه تحت مجوز MIT منتشر شده است.
