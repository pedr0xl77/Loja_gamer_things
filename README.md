# Loja_gamer_things

proxima etapa para evolução do crud:

Gerenciamento de conexões (Context Managers): Em vez de abrir a conexão e lembrar de dar .close() manualmente no final, você pode usar o bloco with. Ele garante que o banco feche sozinho mesmo se o código der algum erro inesperado no meio do caminho.

Variáveis de Ambiente: No arquivo de conexão, sua senha do banco de dados está exposta (password="12345678"). No futuro, aprender a usar uma biblioteca como python-dotenv para esconder essas credenciais em um arquivo .env vai deixar seu projeto com nível profissional de segurança.