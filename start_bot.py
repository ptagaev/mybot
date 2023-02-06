from aiogram.utils import executor
from bot import dp
from tables import register_handlers_admin

#
# client.register_handlers_client(dp)
# other.register_handlers_other(dp)
# admin.register_handlers_admin(dp)
register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True)