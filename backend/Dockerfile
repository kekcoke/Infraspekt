FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
# Switch to install for better compatibility in alpine environments
RUN npm install --omit=dev

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY src/ ./src/
EXPOSE 3001
ENV NODE_ENV=production
USER node
CMD ["node", "src/server.js"]
