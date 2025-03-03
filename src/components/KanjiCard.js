import React from 'react';

const KanjiCard = ({ kanji }) => {
  if (!kanji) return null;

  // Split kanji and annotation using regex
  const [mainKanji, annotation] = kanji.kanji.split(/\(([^)]+)\)/);

  return (
    <div className="card" id="card">
      <span className="kanji-main">
        {mainKanji}
        {annotation && <span className="kanji-annotation">({annotation})</span>}
      </span>
    </div>
  );
};

export default KanjiCard;