from environs import Env

database_name = 'db1.db'
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

skip_updates = True

log_chat = ''
errors_chat_id = ''
