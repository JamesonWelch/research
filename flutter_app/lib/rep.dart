
import 'package:flutter/material.dart';

Checkbox(
value: true,
onChanged: (bool val) => print(val)
),

SearchType _searchType;
Radio<SearchType>(
groupValue: _searchType,
value: SearchType.anywhere,
onChanged: (SearchType val) => _searchType = val),
const Text('Search Anywhere'),
Radio<SearchType>(
groupValue: _searchType,
value: SearchType.text,
onChanged: (SearchType val) => _searchType = val)
),

FormField<String>(
builder: (FormFieldState<String> state) {
  return TextField();
},
onSaved: (String initialValue) {
  //kjklasjdf
},
validator: (String val) {
  // validation logic
}
)

GlobalKey<FormState> _key = GlobalKey<FormState>();
@override
Widget build(BuildContext context) {
  return Form(
    key: _key,
    autovalidate: true,
    child: //data
  )
}


void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.black,
      ),
      home: MyHomePage(title: 'Flutter Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key:key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  in _counter = 0;
  void _incrementCounter() {
    setState(() {
      _counter ++;
  });
  }
}

@override
Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(
      title: Text(widget.title),
    ),
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(
            'You have pressed the button:'
          ),
          Text(
            '$_counter',
            style: Theme.of(context).textTheme.headline4,
          ),
        ],
        ),
      ),
    floatingActionButton: FloatingActionButton(
      onPressed: _incrementCounter,
      toolip: 'Increment',
      child: Icon(Icons.add),
    )
  )
}


Widget build(BuildContext context) {
  return Person(firstName:"Jameson", lastName:"Welch");
}

class Person extends StatelessWidget {
  final String firstName;
  final String lastName;
  Person({this.firstName, this.lastName}) {}
  Widget build(BuildContext context) {
    retrun Container(child: Text('$firstName $lastName'));
  }
}

Image.asset('assets/img.jpg', fit: BoxFit.contain,),

const Text('Search Terms'),
TextField(
onChanged: (String val) => _searchTerm = val,
),

TextEditingController _controller =
    TextEditingController(text: 'Initial Text Value');
const Text('Search Terms'),
TextField(
controller: _controller,
onChanged: (String val) => _searchTerm = val,
),

return TextField(
controller: _emailDecoration(
labelText: 'Email',
hintText: 'email@email.com',
icon: Icon(Icons.contact_email),
),
),

return TextField(
obscureText: true,
decoration: InputDecoration(
labelText: 'Password',
),
);