FROM node:24-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY src ./src
EXPOSE 3001
ENV NODE_ENV=production
USER node
CMD ["node", "src/server.js"]
# Force rebuild Thu Jun 11 10:57:51 PDT 2026
