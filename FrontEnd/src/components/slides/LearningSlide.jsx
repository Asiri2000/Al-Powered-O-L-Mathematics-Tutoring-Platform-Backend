import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';

export default function LearningSlide({ stepData, onNext }) {
  const [selectedOption, setSelectedOption] = useState(null);
  const [status, setStatus] = useState('idle'); // 'idle' | 'correct' | 'wrong'
  const [isImageOpen, setIsImageOpen] = useState(false);
  const [isImageVisible, setIsImageVisible] = useState(true);

  const handleCheck = () => {
    // Find the selected option object
    const option = stepData.options.find(opt => opt.id === selectedOption);
    
    if (option?.is_correct) {
      setStatus('correct');
      // Optional: new Audio('/sounds/correct.mp3').play();
    } else {
      setStatus('wrong');
      // Optional: new Audio('/sounds/wrong.mp3').play();
    }
  };

  useEffect(() => {
    if (!isImageOpen) return;
    const onKey = (e) => { if (e.key === 'Escape') setIsImageOpen(false); };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [isImageOpen]);

  // Hide image by default on smaller screens so options remain visible without scrolling
  useEffect(() => {
    setIsImageVisible(window.innerWidth >= 768);
  }, []);

  return (
    <div className="flex flex-col h-full max-w-3xl mx-auto p-6 gap-4">
      
      {/* --- TOP SECTION: THEORY CARD --- */}
      {/* Only show if theory_text exists */}
      {stepData.theory_text && (
        <motion.div
          initial={{ y: -10, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-lg shadow-md flex flex-col md:flex-row items-center gap-4"
        >
          <div className="md:w-1/2 flex flex-col">
            <div className="flex items-start justify-between">
              <h3 className="text-sm font-bold text-blue-700 uppercase tracking-wide mb-2">
                Quick Tip
              </h3>

              {stepData.theory_media_url && (
                <button
                  onClick={() => setIsImageVisible(v => !v)}
                  className="text-xs text-blue-600 underline md:hidden ml-2"
                >
                  {isImageVisible ? 'Hide image' : 'Show image'}
                </button>
              )}
            </div>

            <p className="text-gray-700 text-sm leading-relaxed">
              {stepData.theory_text}
            </p>

            {stepData.theory_media_url && !isImageVisible && (
              <div className="mt-2 md:hidden">
                <button onClick={() => setIsImageVisible(true)} className="text-sm text-blue-600 underline">Show image</button>
              </div>
            )}
          </div>

          {stepData.theory_media_url && isImageVisible && (
            <>
              <motion.img
                whileHover={{ scale: 1.02 }}
                onClick={() => setIsImageOpen(true)}
                src={stepData.theory_media_url}
                alt="Visual Aid"
                className="md:w-1/2 w-full rounded-md max-h-[40vh] md:max-h-[56vh] h-auto object-contain bg-white shadow-sm cursor-zoom-in"
              />

              {isImageOpen && (
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50"
                  onClick={() => setIsImageOpen(false)}
                >
                  <motion.img
                    initial={{ scale: 0.98 }}
                    animate={{ scale: 1 }}
                    src={stepData.theory_media_url}
                    alt="Full Visual"
                    className="max-w-[95vw] max-h-[95vh] object-contain rounded-md shadow-xl"
                    onClick={(e) => e.stopPropagation()}
                  />
                </motion.div>
              )}
            </>
          )}
        </motion.div>
      )}

      {/* --- MIDDLE SECTION: QUESTION --- */}
      <div className="flex-1 flex flex-col justify-center overflow-visible">
        <h2 className="text-2xl md:text-3xl font-bold text-gray-800 mb-4 text-center md:text-left">
          {stepData.question_text}
        </h2> 

        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.45 }}
          className="pr-2 pb-2"
        >
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {stepData.options.map((option) => (
              <motion.button
                key={option.id}
                whileTap={{ scale: 0.98 }}
                whileHover={{ scale: 1.02 }}
                transition={{ type: 'spring', stiffness: 300, damping: 20 }}
                onClick={() => status === 'idle' && setSelectedOption(option.id)}
                className={`w-full p-3 md:p-4 rounded-xl border-2 text-left md:text-left font-medium text-sm md:text-base transition-all shadow-sm ${
                  selectedOption === option.id
                    ? status === 'correct'
                      ? 'bg-green-100 border-green-500 text-green-800 ring-2 ring-green-200'
                      : status === 'wrong'
                        ? 'bg-red-100 border-red-500 text-red-800 ring-2 ring-red-200'
                        : 'bg-blue-50 border-blue-400 text-blue-800 ring-2 ring-blue-200'
                    : 'bg-white border-gray-200 hover:bg-gray-50 hover:shadow-md'
                }`}
              >
                <div className="break-words">{option.option_text}</div>
              </motion.button>
            ))}
          </div>
        </motion.div>
      </div>

      {/* --- BOTTOM SECTION: ACTION BUTTON --- */}
      <div className="sticky bottom-0 bg-white pt-3 border-t border-gray-100 mt-2 pb-4">
        {status === 'idle' ? (
          <motion.button 
            whileHover={{ scale: 1.02 }}
            onClick={handleCheck}
            disabled={!selectedOption}
            className="w-full py-3 rounded-xl bg-gray-900 text-white font-bold disabled:opacity-50 hover:bg-black transition-colors"
          >
            CHECK ANSWER
          </motion.button>
        ) : (
          <motion.button 
            initial={{ scale: 0.9, opacity: 0.9 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ type: 'spring', stiffness: 260, damping: 22 }}
            onClick={() => {
                // Reset state for next slide
                setStatus('idle');
                setSelectedOption(null);
                onNext(status === 'correct');
            }}
            className={`w-full py-3 rounded-xl text-white font-bold shadow-lg ${
              status === 'correct' ? 'bg-green-500 hover:bg-green-600' : 'bg-red-500 hover:bg-red-600'
            }`}
          >
            {status === 'correct' ? 'CONTINUE' : 'GOT IT'}
          </motion.button>
        )}
      </div>
    </div>
  );
}