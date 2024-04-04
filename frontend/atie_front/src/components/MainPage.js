import  React, {useEffect, useState} from "react"
import '../style/media.css'
import '../style/App.css'


const MainPage = ({setIsLight}) => {


    useEffect(() => {
        setIsLight(false)
    }, [])

    return (
        <div className="mainpage">
            <section className="hero d-flex justify-center flex-column align-items">
                <div className="hero__main container d-flex align-center justify-center  flex-column">
                    <h1 className="hero__title"><span class="bold">ATIE</span> </h1>
                    <h2 className="hero__subtitle ">MarketPlace</h2>
                </div>
                <button className="orange_btn">Купить раба</button>
            </section>

        </div>
    )

}


export default MainPage