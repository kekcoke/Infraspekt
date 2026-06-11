FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
# Use built-in npm with clean install
RUN npm ci --only=production

FROM node:20-alpine AS runtime
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY src/ ./src/
EXPOSE 3001
ENV NODE_ENV=production
USER node
CMD ["node", "src/server.js"]
