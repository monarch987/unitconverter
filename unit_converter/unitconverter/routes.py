from flask import render_template,redirect,url_for,flash,request
from unitconverter.forms import(LengthForm,WeightForm,TemperatureForm)
from unitconverter import app
from unitconverter import db



@app.route("/")
@app.route("/length", methods=["GET","POST"])
def length():

    form = LengthForm()
   
    if form.validate_on_submit():
        
        from_unit = form.dropdown.data
        to_unit = form.dropdown_2.data
        value = form.value.data
        if value:

            factor = db.get_conversion(from_unit,to_unit,'length_conversion')
            output = value*factor

        else:
            return

        source='length'

        print(f"Received Input: {value} {from_unit} → {output} {to_unit}")  # Debugging

        return redirect(url_for('results',from_unit=from_unit,to_unit=to_unit,value=value,output=output,source=source))

    return render_template('length.html',form=form)


@app.route("/weight",methods=["GET","POST"])
def weight():

    form = WeightForm()
   
    if form.validate_on_submit():
        
        from_unit = form.dropdown.data
        to_unit = form.dropdown_2.data
        value = form.value.data
        if value:

            factor = db.get_conversion(from_unit,to_unit,'weight_conversion')
            output = value*factor

        else:
            return

        source='weight'

        print(f"Received Input: {value} {from_unit} → {output} {to_unit}")  # Debugging

        return redirect(url_for('results',from_unit=from_unit,to_unit=to_unit,value=value,output=output,source=source))


    return render_template('weight.html',form=form)


@app.route("/temperature",methods=["GET","POST"])
def temperature():

    form = TemperatureForm()
   
    if form.validate_on_submit():
        
        from_unit = form.dropdown.data
        to_unit = form.dropdown_2.data
        value = form.value.data
        if value:

            factor = db.get_conversion(from_unit,to_unit,'temperature_conversion')
            output = value*factor

        else:
            return

        source='temperature'

        print(f"Received Input: {value} {from_unit} → {output} {to_unit}")  # Debugging

        return redirect(url_for('results',from_unit=from_unit,to_unit=to_unit,value=value,output=output,source=source))

    

    return render_template('temperature.html',form=form)


@app.route("/results")
def results():

    from_unit = request.args.get('from_unit')
    to_unit = request.args.get('to_unit')
    value = request.args.get('value')
    result = request.args.get('output')
    source = request.args.get('source')

    print(f"Rendering results: {value} {from_unit} → {result} {to_unit}")  # Debugging
    
    return render_template('results.html',from_unit=from_unit,to_unit=to_unit,value=value,result=result,source=source)