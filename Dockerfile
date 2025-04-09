# Используем официальный образ Python
FROM python:3.10.6-slim-bullseye

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg curl unzip fonts-liberation libasound2 libatk-bridge2.0-0 libcups2 libdbus-1-3 \
    libgtk-3-0 libgbm1 libnss3 libvulkan1 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libxrender1 \
    libxshmfence1 libx11-xcb1 libx11-6 libxext6 xdg-utils openjdk-17-jre logrotate \
    && rm -rf /var/lib/apt/lists/*

# Установка Chrome (стабильная версия)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Установка ChromeDriver (совместимая версия)
RUN CHROME_VERSION=$(google-chrome-stable --version | grep -oP '\d+\.\d+\.\d+\.\d+') && \
    CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION%%.*}") && \
    wget -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /usr/local/bin/chromedriver-linux64

# Установка Allure
RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.zip \
    && unzip -q allure-2.27.0.zip -d /opt/ \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure-2.27.0.zip

# Копируем код приложения
WORKDIR /app
COPY . .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Команда по умолчанию
CMD ["pytest ", "./tests/ -n auto"]