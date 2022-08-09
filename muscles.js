const fs = require('fs/promises')

async function main(){    
    const datJSON = await fs.readFile('./jsons/exercises-2.json',{ encoding: 'utf8' })
    const data = JSON.parse(datJSON)

    const musclesArrays = data.map( exe => {
        console.log('\t',{exe})
        return exe.muscles
    })

    const musculos = musclesArrays.reduce((acc, curr)=>{
        curr.forEach(e => {
            acc.push(e)
        });

        return acc
    },[])

    const musculos_unique = [... new Set(musculos)]

    fs.writeFile('./jsons/muscles-2.json', JSON.stringify(musculos_unique))
}

main()