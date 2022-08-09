const fs = require('fs/promises');
function help(){
    const {one, two} =require('./node')
    

    const exerciciosOne = one.map(e => e.name)

    let exercicios_que_nao_estao = []

    function verificaSeExisteNaLista(exercicioTwo, muscNome){
        let verify = exerciciosOne.indexOf(exercicioTwo.name) > -1

        if(!verify) {
            exercicioTwo.muscles = [muscNome]
            exercicios_que_nao_estao.push(exercicioTwo)
        }
        return verify
    }

    two.forEach(musc => {
        nomeMusc = Object.keys(musc)[0]
        musc[nomeMusc].forEach(e => {
            verificaSeExisteNaLista(e, nomeMusc)
        })

    })

    newExercises = exercicios_que_nao_estao.reduce((acc, curr, index)=>{
        let list = listExer(acc)
        jaexiste = list.indexOf(curr.name) 
        if(jaexiste > -1){
            //console.log({'acc':acc[jaexiste], 'curr': curr}, '\n')
            acc[jaexiste].muscles.push(curr.muscles[0])
        }else{
            acc.push(curr)
        }
        return acc
    }, [])

    //console.log(newExercises)

    function listExer(arr){
        return arr.map(e=>e.name)
    }

    return newExercises
}

async function main(){
    const newExercises = help()
    const dataJson = await fs.readFile('./jsons/exercises.json',{ encoding: 'utf8' })
    const data = JSON.parse(dataJson)    
    let cont = 26
    newExercises.forEach(e => {
        e.id = cont
        data.push(e)
        cont++
    })

    writeFileJson(JSON.stringify(data))
    
}

main()

async function writeFileJson(Json){
    await fs.writeFile('./jsons/exercises-2.json', Json)
}