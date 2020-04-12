import covid_india

from covid_india import states
from userbot import client
from userbot.utils.events import NewMessage

plugin_category = "pandemic"

# Defining Active Cases
active_case = f"{%(Total)s - %(Cured)s + %(Death)s}"

cov_str = f"""`{'Confirmed':<9}:` **%(Total)s**
`{'Active':<9}:` **active_case**
`{'Recovered':<9}:`  **%(Cured)s**
`{'Deaths':<9}:`  **%(Death)s**"""

cdict = {
    'AN':'Andaman and Nicobar Islands',
    'AP':'Andhra Pradesh', 'AR':'Arunachal Pradesh',
    'AS':'Assam','BR':'Bihar','CH':'Chandigarh',
    'CG':'Chhattisgarh','DL':'Delhi','GA':'Goa',
    'GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh',
    'JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka',
    'KL':'Kerala','MP':'Madhya Pradesh','MH':'Maharashtra',
    'MN':'Manipur','ML':'Mizoram','OR':'Odisha','PY':'Puducherry',
    'PB':'Punjab','RJ':'Rajasthan','TN':'Tamil Nadu','TG':'Telengana',
    'TR':'Tripura','UP':'Uttar Pradesh','UK':'Uttarakhand','WB':'West Bengal'
}

@client.onMessage(
    command="corona",
    outgoing=True, regex="(?:corona_in|covin)(?: |$)(.*)"
)
async def ncov(event: NewMessage.Event) -> None:
    """Testing"""
    covid = covid_india
    catch = event.matches[0]
    match = event.matches[0].group(1)
    if match:
        strings = []
        failed = []
        args, c = await client.parse_arguments(match)
        
        if match.lower() == "states":
            strings = sorted(covid.states.getdata())
        else:
            for c in args:
                try:
                    await event.answer("`Parsing data...`")
                    state = (cdict[c.upper()] if c.upper() in cdict else c.title())
                    state_data = covid.states.getdata(state)
                    string = f"COVID-19 stats for:  `{state}`\n"
                    string += cov_str % state_data
                    strings.append(string)
                except KeyError:
                    failed.append(state)
                    continue
        if strings:
            await event.answer('\n\n'.join(strings))
        if failed:
            await event.answer(f"Couldn't find stats for: `{state}`.\nDouble check for spelling errors.")
    if not match:
        await event.edit("**Usage**: `.covin 'State/Abbrevation'`.")
        return
        
