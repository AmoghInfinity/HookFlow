import { useState, useCallback, useRef } from 'react'
import InputForm from './components/InputForm'
import OutputPanel from './components/OutputPanel'

const API_URL = `${import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'}/generate`

export default function App() {
  const [data, setData] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const lastFormValues = useRef(null)

  const handleGenerate = useCallback(async (formValues) => {
    lastFormValues.current = formValues
    setIsLoading(true)
    setError(null)

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formValues),
      })

      if (!res.ok) throw new Error(`Server responded with ${res.status}`)

      const json = await res.json()

      if (json.status === 'success' && json.data) {
        setData(json.data)
      } else {
        throw new Error('Unexpected response format')
      }
    } catch (err) {
      setError(err.message || 'Something went wrong. Try again.')
    } finally {
      setIsLoading(false)
    }
  }, [])

  const handleRegenerate = useCallback(() => {
    if (lastFormValues.current) {
      handleGenerate(lastFormValues.current)
    }
  }, [handleGenerate])

  return (
    <div className="app-layout">
      <InputForm onSubmit={handleGenerate} isLoading={isLoading} />
      <OutputPanel data={data} isLoading={isLoading} error={error} onRegenerate={handleRegenerate} />
    </div>
  )
}
