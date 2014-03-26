   $(document).ready(function() {
    var numbers;
    var countries = new Bloodhound({
        datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.name); },
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        limit: 10,
        local: [
            { name: 'Andorra' },
            { name: 'United Arab Emirates' },
            { name: 'Afghanistan'},
            { name: 'Antigua and Barbuda'},
            { name: 'Anguilla'},
        ]
    });

countries.initialize();

$('.countries .typeahead').typeahead(null, {
  displayKey: 'name',
  source: countries.ttAdapter()
});

});