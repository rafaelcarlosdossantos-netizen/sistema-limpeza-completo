import { useState, useEffect } from 'react'

function App() {
  const [view, setView] = useState('login')
  const [isLogged, setIsLogged] = useState(false)
  const [status, setStatus] = useState('Conectando...')
  const [servicos, setServicos] = useState([])
  const [loginData, setLoginData] = useState({ usuario: '', senha: '' })
  const [novoCliente, setNovoCliente] = useState({ cliente: '', data: '', valor: '' })
  const [editandoServico, setEditandoServico] = useState(null) // Estado para o serviço sendo editado
  
  const API_BASE = 'https://sistema-limpeza-completo.vercel.app/api'

  // BUSCAR DADOS DO SERVIDOR
  const carregarServicos = ( ) => {
    fetch(`${API_BASE}/servicos`)
      .then(res => res.json())
      .then(data => {
        setServicos(data)
        setStatus('Sistema Online')
      })
      .catch(() => setStatus('Erro na conexão'))
  }

  // FUNÇÃO DE LOGIN
  const handleLogin = (e) => {
    e.preventDefault()
    fetch(`${API_BASE}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(loginData)
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        setIsLogged(true)
        setView('painel')
        carregarServicos()
      } else {
        alert('Usuário ou senha incorretos!')
      }
    })
    .catch(() => alert('Erro ao conectar com o servidor'))
  }

  // SALVAR NO BANCO DE DADOS
  const handleSalvar = (e) => {
    e.preventDefault()
    fetch(`${API_BASE}/servicos`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(novoCliente)
    })
    .then(res => res.json())
    .then(() => {
      carregarServicos()
      setNovoCliente({ cliente: '', data: '', valor: '' })
      setView('painel')
      alert('Agendamento salvo com sucesso!')
    })
  }

  // FUNÇÃO PARA EDITAR SERVIÇO
  const handleEditar = (servico) => {
    setEditandoServico({ ...servico }) // Copia o serviço para edição
  }

  // FUNÇÃO PARA SALVAR EDIÇÃO
  const handleSalvarEdicao = (e) => {
    e.preventDefault()
    fetch(`${API_BASE}/servicos/${editandoServico.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(editandoServico)
    })
    .then(res => res.json())
    .then(() => {
      carregarServicos()
      setEditandoServico(null) // Fecha o modal de edição
      alert('Serviço atualizado com sucesso!')
    })
    .catch(() => alert('Erro ao atualizar serviço'))
  }

  // FUNÇÃO PARA EXCLUIR SERVIÇO
  const handleExcluir = (id) => {
    if (window.confirm('Tem certeza que deseja excluir este agendamento?')) {
      fetch(`${API_BASE}/servicos/${id}`, {
        method: 'DELETE',
      })
      .then(() => {
        carregarServicos()
        alert('Serviço excluído com sucesso!')
      })
      .catch(() => alert('Erro ao excluir serviço'))
    }
  }

  // --- TELA DE LOGIN ---
  if (!isLogged) {
    return (
      <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px', fontFamily: 'sans-serif' }}>
        <div style={{ maxWidth: '350px', width: '100%', backgroundColor: 'white', borderRadius: '12px', boxShadow: '0 10px 25px rgba(0,0,0,0.1)', padding: '40px' }}>
          <h1 style={{ fontSize: '22px', fontWeight: 'bold', color: '#2563eb', marginBottom: '25px', textAlign: 'center' }}>Acesso ao Sistema</h1>
          <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <input required placeholder="Usuário" value={loginData.usuario} onChange={e => setLoginData({...loginData, usuario: e.target.value})} style={{ padding: '12px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <input required type="password" placeholder="Senha" value={loginData.senha} onChange={e => setLoginData({...loginData, senha: e.target.value})} style={{ padding: '12px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <button type="submit" style={{ padding: '12px', backgroundColor: '#2563eb', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Entrar</button>
          </form>
          <p style={{ fontSize: '11px', color: '#9ca3af', marginTop: '20px', textAlign: 'center' }}>Status: {status}</p>
        </div>
      </div>
    )
  }

  // --- TELA DE NOVO AGENDAMENTO ---
  if (view === 'novo') {
    return (
      <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', padding: '40px', fontFamily: 'sans-serif' }}>
        <div style={{ maxWidth: '500px', margin: '0 auto', backgroundColor: 'white', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}>
          <h2 style={{ marginBottom: '20px', color: '#1e3a8a' }}>Novo Agendamento</h2>
          <form onSubmit={handleSalvar} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <input required placeholder="Nome do Cliente" value={novoCliente.cliente} onChange={e => setNovoCliente({...novoCliente, cliente: e.target.value})} style={{ padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <input required type="date" value={novoCliente.data} onChange={e => setNovoCliente({...novoCliente, data: e.target.value})} style={{ padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <input required placeholder="Valor (ex: R$ 150,00)" value={novoCliente.valor} onChange={e => setNovoCliente({...novoCliente, valor: e.target.value})} style={{ padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db' }} />
            <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
              <button type="submit" style={{ flex: 1, padding: '12px', backgroundColor: '#10b981', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Salvar</button>
              <button type="button" onClick={() => setView('painel')} style={{ flex: 1, padding: '12px', backgroundColor: '#6b7280', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Cancelar</button>
            </div>
          </form>
        </div>
      </div>
    )
  }

  // --- TELA DO PAINEL ---
  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f3f4f6', padding: '40px', fontFamily: 'sans-serif' }}>
      <div style={{ maxWidth: '900px', margin: '0 auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
          <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: '#1e3a8a' }}>Painel de Serviços</h1>
          <button onClick={() => {setIsLogged(false); setView('login')}} style={{ padding: '8px 16px', backgroundColor: '#ef4444', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>Sair</button>
        </div>
        <div style={{ backgroundColor: 'white', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)', padding: '20px' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid #f3f4f6', textAlign: 'left' }}>
                <th style={{ padding: '12px', color: '#6b7280' }}>Cliente</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Data</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Status</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Valor</th>
                <th style={{ padding: '12px', color: '#6b7280' }}>Ações</th> {/* Nova coluna de Ações */}
              </tr>
            </thead>
            <tbody>
              {servicos.map(s => (
                <tr key={s.id} style={{ borderBottom: '1px solid #f3f4f6' }}>
                  <td style={{ padding: '12px', fontWeight: '500' }}>{s.cliente}</td>
                  <td style={{ padding: '12px' }}>{s.data}</td>
                  <td style={{ padding: '12px' }}><span style={{ padding: '4px 8px', borderRadius: '12px', fontSize: '12px', backgroundColor: s.status === 'Concluído' ? '#dcfce7' : '#fef9c3', color: s.status === 'Concluído' ? '#166534' : '#854d0e' }}>{s.status}</span></td>
                  <td style={{ padding: '12px' }}>{s.valor}</td>
                  <td style={{ padding: '12px' }}>
                    <button onClick={() => handleEditar(s)} style={{ padding: '6px 10px', backgroundColor: '#2563eb', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', marginRight: '5px' }}>Editar</button>
                    <button onClick={() => handleExcluir(s.id)} style={{ padding: '6px 10px', backgroundColor: '#ef4444', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>Excluir</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button onClick={() => setView('novo')} style={{ marginTop: '20px', width: '100%', padding: '12px', backgroundColor: '#10b981', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>+ Novo Agendamento</button>
        </div>
      </div>

      {/* Modal de Edição */}
      {editandoServico && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ backgroundColor: 'white', padding: '30px', borderRadius: '12px', boxShadow: '0 5px 15px rgba(0,0,0,0.3)', maxWidth: '400px', width: '100%' }}>
            <h2 style={{ marginBottom: '20px', color: '#1e3a8a' }}>Editar Agendamento</h2>
            <form onSubmit={handleSalvarEdicao} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
              <label>Cliente:
                <input required value={editandoServico.cliente} onChange={e => setEditandoServico({...editandoServico, cliente: e.target.value})} style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db', marginTop: '5px' }} />
              </label>
              <label>Data:
                <input required type="date" value={editandoServico.data} onChange={e => setEditandoServico({...editandoServico, data: e.target.value})} style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db', marginTop: '5px' }} />
              </label>
              <label>Valor:
                <input required value={editandoServico.valor} onChange={e => setEditandoServico({...editandoServico, valor: e.target.value})} style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db', marginTop: '5px' }} />
              </label>
              <label>Status:
                <select value={editandoServico.status} onChange={e => setEditandoServico({...editandoServico, status: e.target.value})} style={{ width: '100%', padding: '10px', borderRadius: '6px', border: '1px solid #d1d5db', marginTop: '5px' }}>
                  <option value="Agendado">Agendado</option>
                  <option value="Concluído">Concluído</option>
                  <option value="Cancelado">Cancelado</option>
                </select>
              </label>
              <div style={{ display: 'flex', gap: '10px', marginTop: '20px' }}>
                <button type="submit" style={{ flex: 1, padding: '12px', backgroundColor: '#10b981', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Salvar Edição</button>
                <button type="button" onClick={() => setEditandoServico(null)} style={{ flex: 1, padding: '12px', backgroundColor: '#6b7280', color: 'white', border: 'none', borderRadius: '6px', fontWeight: '600', cursor: 'pointer' }}>Cancelar</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
