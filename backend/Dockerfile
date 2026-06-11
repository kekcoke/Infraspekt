FROM node:24-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY src ./src
EXPOSE 3001
ENV NODE_ENV=production
USER node
CMD ["node", "src/server.js"]
