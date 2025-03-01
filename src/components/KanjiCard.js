import React from 'react';

const KanjiCard = ({ kanji }) => {
  return (
    <div className="card" id="card">
      {kanji ? kanji.kanji : 'Loading...'}
    </div>
  );
};

export default KanjiCard;