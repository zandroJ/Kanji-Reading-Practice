const kanjiData = [];

// Load the Kanji data from the external JSON file
fetch('./kanojo.json')
  .then(response => response.json())
  .then(data => {
    kanjiData.push(...data);
    initializeGame(); // Call the game logic once the data is fetched
  })
  .catch(err => console.error('Error loading JSON:', err));

function initializeGame() {
  const global = {
    kanjiData,
    originalKanjiData: JSON.parse(JSON.stringify(kanjiData)), // Keep original for progress tracking
    score: 0,
    progress: 0,
    currentKanji: null,
  };

  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }

  function getNextCard() {
    if (kanjiData.length === 0) {
      alert(`Game Over! Your score: ${global.score}/${global.originalKanjiData.length}`);
      resetGame();
      return null;
    }

    const kanji = kanjiData[Math.floor(Math.random() * kanjiData.length)];
    // Remove the chosen kanji from the list to avoid reusing it
    kanjiData.splice(kanjiData.indexOf(kanji), 1);
    shuffle(kanjiData); // Shuffle remaining kanjiData before returning
    return kanji;
  }

  function displayKanji(kanji) {
    document.getElementById('card').innerHTML = kanji.kanji;
    global.currentKanji = kanji;
    document.getElementById('answerInput').value = ''; // Clear input field
    document.getElementById('feedback').innerText = ''; // Clear feedback
  }

  function checkAnswer() {
    const userInput = document.getElementById('answerInput').value.trim().toLowerCase();
    if (!global.currentKanji) return;

    // Split the readings by comma and check if the user input matches any
    const correctReadings = global.currentKanji.reading.split(', ').map(r => r.trim().toLowerCase());
    const correct = correctReadings.includes(userInput);

    const feedbackMessage = correct
      ? `✅ Correct!`
      : `❌ Wrong! Correct: ${global.currentKanji.reading}`;

    const meaningMessage = `Meaning: ${global.currentKanji.meaning}`;

    // Display feedback and meaning
    document.getElementById('feedback').innerHTML = `${feedbackMessage}<br>${meaningMessage}`;

    // Play the corresponding sound
    const feedbackSound = correct ? document.getElementById('correctSound') : document.getElementById('wrongSound');
    feedbackSound.play();

    updateScore(correct);

    // Wait for feedback before moving to next card
    setTimeout(() => nextCard(), 2000);
}


  function updateScore(correct) {
    if (correct) {
      global.score++;
      document.getElementById('score').textContent = global.score;
    }

    // Always increase the progress even if the answer is wrong
    global.progress += 100 / global.originalKanjiData.length;
    document.getElementById('progress').style.width = `${Math.min(global.progress, 100)}%`;

    // End the game if all kanji are answered
    if (kanjiData.length === 0) {
      alert(`Congratulations! You have answered all the kanji! Your Score: ${global.score}`);
      resetGame();
    }
  }

  function resetGame() {
    global.score = 0;
    global.progress = 0;
    document.getElementById('score').textContent = '0';
    document.getElementById('progress').style.width = '0%';

    // Restore the original Kanji data and shuffle again
    kanjiData.push(...global.originalKanjiData);
    shuffle(kanjiData);
  }

  function nextCard() {
    global.currentKanji = getNextCard();
    if (global.currentKanji) {
      displayKanji(global.currentKanji);
    }
  }

  // Start the game
  nextCard();

  // Event listeners
  document.getElementById('submitButton').addEventListener('click', checkAnswer);
  document.getElementById('nextButton').addEventListener('click', nextCard);
  document.getElementById('answerInput').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevent form submission if inside a form
      checkAnswer();
    }
  });
}
