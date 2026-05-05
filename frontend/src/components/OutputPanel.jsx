import SectionCard from './SectionCard'

function SkeletonCard() {
  return (
    <div className="skeleton-card">
      <div className="skeleton-header">
        <div className="skeleton-icon" />
        <div className="skeleton-title" />
      </div>
      <div className="skeleton-line" />
      <div className="skeleton-line" />
      <div className="skeleton-line" />
    </div>
  )
}

function WelcomeState() {
  return (
    <div className="welcome-state">
      <div className="welcome-icon">✦</div>
      <h2>Ready to create?</h2>
      <p>Fill in your content details on the left and hit Generate. HookFlow will craft scroll-stopping hooks, a polished script, captions, hashtags, and a shot list — all in seconds.</p>
      <div className="welcome-steps">
        <div className="welcome-step">
          <span className="welcome-step-num">1</span>
          <span>Describe your topic</span>
        </div>
        <div className="welcome-step">
          <span className="welcome-step-num">2</span>
          <span>Set tone &amp; style</span>
        </div>
        <div className="welcome-step">
          <span className="welcome-step-num">3</span>
          <span>Generate content</span>
        </div>
      </div>
    </div>
  )
}

export default function OutputPanel({ data, isLoading, error, onRegenerate }) {
  if (isLoading) {
    return (
      <main className="main-panel">
        <div className="skeleton-wrap">
          {[...Array(5)].map((_, i) => <SkeletonCard key={i} />)}
        </div>
      </main>
    )
  }

  if (!data && !error) {
    return (
      <main className="main-panel">
        <WelcomeState />
      </main>
    )
  }

  return (
    <main className="main-panel">
      {error && (
        <div className="error-banner">
          <span>⚠</span>
          {error}
        </div>
      )}
      {data && (
        <>
          <SectionCard type="hooks" data={data} onRegenerate={onRegenerate} />
          <SectionCard type="script" data={data} onRegenerate={onRegenerate} />
          <SectionCard type="caption" data={data} onRegenerate={onRegenerate} />
          <SectionCard type="hashtags" data={data} onRegenerate={onRegenerate} />
          <SectionCard type="shotList" data={data} onRegenerate={onRegenerate} />
        </>
      )}
    </main>
  )
}
