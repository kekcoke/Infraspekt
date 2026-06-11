FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
# Update npm and perform a clean install for production
RUN npm install -g npm@latest && npm install --production

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY src/ ./src/
EXPOSE 3001
ENV NODE_ENV=production
USER node
CMD ["node", "src/server.js"]
