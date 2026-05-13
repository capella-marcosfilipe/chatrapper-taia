export default function LoadingDots() {
  return (
    <div className="loading visible" style={{ alignSelf: 'flex-start', marginTop: '10px' }}>
      processando<span className="dot">.</span><span className="dot">.</span><span className="dot">.</span>
    </div>
  );
}