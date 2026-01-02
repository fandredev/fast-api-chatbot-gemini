document.addEventListener('DOMContentLoaded', () => {
  const chatForm = document.getElementById('chat-form');
  const userInput = document.getElementById('user-input');
  const chatMessages = document.getElementById('chat-messages');

  const headerAvatarImg = document.getElementById('header-avatar-img');
  const headerAvatarFallback = document.getElementById(
    'header-avatar-fallback'
  );

  const updateHeaderAvatar = async () => {
    try {
      const characterId = Math.floor(Math.random() * 500) + 1;
      const response = await fetch(
        `https://api.jikan.moe/v4/characters/${characterId}`
      );
      if (response.ok) {
        const data = await response.json();
        if (data.data && data.data.images && data.data.images.jpg) {
          const avatarUrl = data.data.images.jpg.image_url;
          headerAvatarImg.src = avatarUrl;
          headerAvatarImg.style.display = 'block';
          headerAvatarFallback.style.display = 'none';
        }
      }
    } catch (error) {
      console.error('Error fetching anime avatar:', error);
    }
  };

  updateHeaderAvatar();

  const healthBanner = document.getElementById('health-banner');
  const checkHealth = async () => {
    try {
      const resp = await fetch('/api/health');
      const data = await resp.json();
      if (data.status === 'quota_exceeded') {
        healthBanner.style.display = 'flex';
        userInput.disabled = true;
        userInput.placeholder = 'Serviço temporariamente indisponível (Cota)';
        document.getElementById('send-btn').disabled = true;
      } else {
        addMessage(
          'Olá! Eu sou o AnimeChat. De qual anime gostaria de falar hoje?',
          false
        );
      }
    } catch (e) {
      console.error('Health Check Error:', e);
      addMessage(
        'Olá! Eu sou o AnimeChat. De qual anime gostaria de falar hoje?',
        false
      );
    }
  };

  checkHealth();

  const getCurrentTime = () => {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  // Rate Limiting Logic
  const rateLimitTimer = document.getElementById('rate-limit-timer');
  const secondsLeftSpan = document.getElementById('seconds-left');
  const sendBtn = document.getElementById('send-btn');
  let countdownInterval = null;

  const getRequestTimestamps = () => {
    const saved = localStorage.getItem('chatRequestTimestamps');
    return saved ? JSON.parse(saved) : [];
  };

  const saveRequestTimestamps = (timestamps) => {
    localStorage.setItem('chatRequestTimestamps', JSON.stringify(timestamps));
  };

  const cleanOldTimestamps = () => {
    const now = Date.now();
    const timestamps = getRequestTimestamps().filter((ts) => now - ts < 60000);
    saveRequestTimestamps(timestamps);
    return timestamps;
  };

  const startCooldown = (timeMs) => {
    if (countdownInterval) clearInterval(countdownInterval);

    rateLimitTimer.style.display = 'flex';
    userInput.disabled = true;
    sendBtn.disabled = true;

    const updateTimer = () => {
      const remaining = Math.ceil((timeMs - (Date.now() - startTime)) / 1000);
      if (remaining <= 0) {
        clearInterval(countdownInterval);
        rateLimitTimer.style.display = 'none';
        // Only re-enable if health banner is not showing
        if (healthBanner.style.display === 'none') {
          userInput.disabled = false;
          sendBtn.disabled = false;
          userInput.placeholder = 'Responder...';
        }
      } else {
        secondsLeftSpan.innerText = remaining;
      }
    };

    const startTime = Date.now();
    secondsLeftSpan.innerText = Math.ceil(timeMs / 1000);
    countdownInterval = setInterval(updateTimer, 1000);
  };

  const checkRateLimit = () => {
    const timestamps = cleanOldTimestamps();
    if (timestamps.length >= 2) {
      const oldestTs = timestamps[0];
      const waitTime = 60000 - (Date.now() - oldestTs);
      if (waitTime > 0) {
        startCooldown(waitTime);
        return false;
      }
    }
    return true;
  };

  // Initialize rate limit state on load
  checkRateLimit();

  const addMessage = (messageData, isUser = false) => {
    const group = document.createElement('div');
    group.classList.add('message-group');
    group.classList.add(isUser ? 'user-group' : 'bot-group');

    const time = getCurrentTime();

    if (isUser) {
      group.innerHTML = `
                <div class="message-content">
                    <div class="bubble user-bubble">${messageData}</div>
                    <span class="timestamp">${time}</span>
                </div>
            `;
    } else {
      group.innerHTML = `
                <div class="message-row">
                    <div class="bot-avatar">
                        <img src="https://ui-avatars.com/api/?name=Assistant&background=e1e4e8&color=70757a" alt="Bot" />
                    </div>
                    <div class="message-content">
                        <span class="sender-name">Assistente</span>
                        <div class="bubble bot-bubble">${
                          messageData.text || messageData
                        }</div>
                        <span class="timestamp">${time}</span>
                    </div>
                </div>
            `;
    }

    chatMessages.appendChild(group);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  };

  const emojiBtn = document.getElementById('emoji-btn');
  const emojiPicker = document.getElementById('emoji-picker');

  // Initialize emoji picker from emoji.js
  if (typeof initEmojiPicker === 'function') {
    initEmojiPicker(userInput, emojiBtn, emojiPicker);
  }

  // Theme Toggle Logic
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const body = document.body;

  // Icons for toggle
  const sunIcon = `
    <circle cx="12" cy="12" r="5"></circle>
    <line x1="12" y1="1" x2="12" y2="3"></line>
    <line x1="12" y1="21" x2="12" y2="23"></line>
    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
    <line x1="1" y1="12" x2="3" y2="12"></line>
    <line x1="21" y1="12" x2="23" y2="12"></line>
    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
  `;

  const moonIcon = `
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
  `;

  themeToggle.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    if (currentTheme === 'dark') {
      body.removeAttribute('data-theme');
      themeIcon.innerHTML = sunIcon;
    } else {
      body.setAttribute('data-theme', 'dark');
      themeIcon.innerHTML = moonIcon;
    }
  });

  chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (!checkRateLimit()) return;

    const message = userInput.value.trim();
    if (!message) return;

    // Add current timestamp to rate limit tracking
    const timestamps = getRequestTimestamps();
    timestamps.push(Date.now());
    saveRequestTimestamps(timestamps);

    // Check if we just hit the limit
    checkRateLimit();

    addMessage(message, true);

    userInput.value = '';

    // Show Typing Indicator
    const typingGroup = document.createElement('div');
    typingGroup.classList.add('message-group', 'bot-group');
    typingGroup.innerHTML = `
      <div class="message-row">
        <div class="bot-avatar">
          <img src="https://ui-avatars.com/api/?name=Assistant&background=e1e4e8&color=70757a" alt="Bot" />
        </div>
        <div class="message-content">
          <span class="sender-name">Assistente</span>
          <div class="bubble bot-bubble typing-status">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
          </div>
        </div>
      </div>
    `;
    chatMessages.appendChild(typingGroup);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      // Remove Typing Indicator
      if (chatMessages.contains(typingGroup)) {
        chatMessages.removeChild(typingGroup);
      }

      if (!response.ok) throw new Error('Server error');

      const data = await response.json();

      if (data.error && data.error.includes('429')) {
        healthBanner.style.display = 'flex';
        userInput.disabled = true;
      } else if (response.status === 429) {
        startCooldown(60000);
      }

      addMessage(data);
    } catch (error) {
      // Remove Typing Indicator on error too
      if (chatMessages.contains(typingGroup)) {
        chatMessages.removeChild(typingGroup);
      }
      console.error('Error:', error);
      addMessage('Ocorreu um erro ao processar sua pergunta sobre animes.');
    }
  });
});
