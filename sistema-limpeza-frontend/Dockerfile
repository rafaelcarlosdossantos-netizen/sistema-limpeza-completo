# Dockerfile para o Frontend do Sistema de Gestão de Limpeza

# Estágio 1: Build da aplicação React
FROM node:20-alpine AS builder

WORKDIR /app

# Copiar arquivos de dependências
COPY package.json pnpm-lock.yaml ./

# Instalar pnpm e dependências
RUN npm install -g pnpm && \
    pnpm install --frozen-lockfile

# Copiar código fonte
COPY . .

# Definir variável de ambiente para produção
ENV VITE_API_URL=http://localhost:5002

# Build da aplicação
RUN pnpm run build

# Estágio 2: Servidor Nginx
FROM nginx:alpine

# Copiar arquivos buildados
COPY --from=builder /app/dist /usr/share/nginx/html

# Copiar configuração customizada do Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expor porta 80
EXPOSE 80

# Comando padrão do Nginx
CMD ["nginx", "-g", "daemon off;"]
