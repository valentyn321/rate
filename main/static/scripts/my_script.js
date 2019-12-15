$('#check').click(function ()) {
$.ajax({
    type: 'GET'.
    url: 'what_rate',
    data: {
        'name': $('#select').val(),
    },
    dataType: 'text',
    cache: false,
    succes: function (data) {
        if (data=='ok') {
            if form.is_valid():
                rate = form.cleaned_data
                print("It's AJAX!")
                if(rate["name"].upper() == "USD/UAH"):
                    purchase = data[0]["buy"]
                    selling = data[0]["sale"]
                    return render(request, 'main/what_rate.html', locals())
                elif(rate["name"].upper() == "EUR/UAH"):
                    purchase = data[1]["buy"]
                    selling = data[1]["sale"]
                    return render(request, 'main/what_rate.html', locals())
                elif(rate["name"].upper() == "RUB/UAH"):
                    purchase = data[2]["buy"]
                    selling = data[2]["sale"]
                    return render(request, 'main/what_rate.html', locals())
                elif(rate["name"].upper() == "BTC/UAH"):
                    purchase = data[3]["buy"]
                    selling = data[3]["sale"]
                    return render(request, 'main/what_rate.html', locals())


        }
        else if (data == 'no'){


        }
    }

});
}