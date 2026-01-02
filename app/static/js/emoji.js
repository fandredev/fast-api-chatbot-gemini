function initEmojiPicker(inputElement, emojiBtn, emojiPicker) {
  if (!inputElement || !emojiBtn || !emojiPicker) return;

  emojiBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    emojiPicker.style.display =
      emojiPicker.style.display === 'none' ? 'grid' : 'none';
  });

  document.addEventListener('click', () => {
    emojiPicker.style.display = 'none';
  });

  emojiPicker.querySelectorAll('span').forEach((emoji) => {
    emoji.addEventListener('click', () => {
      inputElement.value += emoji.textContent;
      inputElement.focus();
    });
  });
}
