import { Link } from 'react-router-dom';
import './App.css'
import { Button, Space } from '@arco-design/web-react';

function App() {

  return (
    <>
      <div>
        <Space size='large'>
          <Button type='primary'>Primary</Button>
          <Button type='secondary'>Secondary</Button>
          <Button type='dashed'>Dashed</Button>
          <Button type='outline'>Outline</Button>
          <Button type='text'>Text</Button>
        </Space>
      </div>
      {/* <div className="site-layout-content">
        <Switch>
          <Route path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
        </Switch>
      </div> */}
    </>
  )
}

export default App
