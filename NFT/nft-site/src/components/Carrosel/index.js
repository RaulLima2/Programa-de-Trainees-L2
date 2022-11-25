import Carousel from 'react-bootstrap/Carousel';

function Carrosel(props) {
    const itens = (() => {
        let array = [];
        for (let i = 0; i < props.itens.length; i++) {
            array.push(
                <Carousel.Item key={i}>
                    <img
                        className="d-block w-100"
                        src={props.itens[i].url}
                        alt={props.itens[i].alt}
                    />
                    <Carousel.Caption>
                        <h3>{props.itens[i].titulo}</h3>
                        <p>{props.itens[i].descricao}</p>
                    </Carousel.Caption>
                </Carousel.Item>
            );
        }
        return array;
    });

  return (
    <Carousel>
        {itens}
    </Carousel>
  );
}

export default Carrosel;