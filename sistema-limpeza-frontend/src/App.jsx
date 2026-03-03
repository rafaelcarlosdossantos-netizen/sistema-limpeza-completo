import { useState } from 'react'
import { Button } from './components/ui/button'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', backgroundColor: '#f3f4f6', fontFamily: 'sans-serif' }}>
      <h1 style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2563eb', marginBottom: '1rem' }}>
        Sistema de Gestão de Limpeza
      </h1>
      <p style={{ color: '#4b5563', marginBottom: '2rem' }}>
        O seu sistema está online e pronto para ser configurado!
      </p>
      <Button onClick={() => setCount((count) => count + 1)}>
        Teste de Botão: {count}
      </Button>
    </div>
  )
}

export default App
