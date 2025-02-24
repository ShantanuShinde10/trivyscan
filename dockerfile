# Use an outdated base image for testing purposes
FROM node:12

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies (some outdated ones for testing vulnerabilities)
RUN npm install

# Copy application source code
COPY . .

# Expose port
EXPOSE 3000

# Start the application
CMD ["node", "server.js"]
