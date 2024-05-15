from discord import SyncWebhook

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1240253508431777812/wa77VSgxaAKuSYGLz5oiZDAiDJpY5oyucr0OJWqlkYzhwkGjeNcM6UnuibJuf3qlli5j")

def send(Text):
    webhook.send(Text)

