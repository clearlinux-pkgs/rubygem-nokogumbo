#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-nokogumbo
Version  : 1.4.2
Release  : 6
URL      : https://rubygems.org/downloads/nokogumbo-1.4.2.gem
Source0  : https://rubygems.org/downloads/nokogumbo-1.4.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rubygem-nokogumbo-lib
BuildRequires : ruby
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-minitest
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rdoc

%description
Nokogumbo - a Nokogiri interface to the Gumbo HTML5 parser.
===========
Nokogumbo provides the ability for a Ruby program to invoke the
[Gumbo HTML5 parser](https://github.com/google/gumbo-parser#readme)
and to access the result as a
[Nokogiri::HTML::Document](http://rdoc.info/github/sparklemotion/nokogiri/Nokogiri/HTML/Document).

%package dev
Summary: dev components for the rubygem-nokogumbo package.
Group: Development
Requires: rubygem-nokogumbo-lib

%description dev
dev components for the rubygem-nokogumbo package.


%package lib
Summary: lib components for the rubygem-nokogumbo package.
Group: Libraries

%description lib
lib components for the rubygem-nokogumbo package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n nokogumbo-1.4.2
gem spec %{SOURCE0} -l --ruby > rubygem-nokogumbo.gemspec

%build
gem build rubygem-nokogumbo.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
nokogumbo-1.4.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/nokogumbo-1.4.2 && ruby -I.:lib test-nokogumbo.rb && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/nokogumbo-1.4.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/HTML5-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/HTML5/cdesc-HTML5.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/HTML5/fragment-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/HTML5/get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/HTML5/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/HTML5/reencode-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogiri/cdesc-Nokogiri.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogumbo/cdesc-Nokogumbo.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/Nokogumbo/parse-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/RbConfig/cdesc-RbConfig.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/ext/nokogumboc/page-Makefile.ri
/usr/lib64/ruby/gems/2.2.0/doc/nokogumbo-1.4.2/ri/ext/nokogumboc/page-char_ref_rl.ri
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/nokogumbo-1.4.2/gem.build_complete
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/nokogumbo-1.4.2/gem_make.out
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/nokogumbo-1.4.2/mkmf.log
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/Makefile
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/attribute.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/attribute.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/attribute.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/char_ref.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/char_ref.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/char_ref.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/char_ref.rl
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/error.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/error.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/error.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/extconf.rb
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/gumbo.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/insertion_mode.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/nokogumbo.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/nokogumbo.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/parser.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/parser.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/parser.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/string_buffer.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/string_buffer.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/string_buffer.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/string_piece.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/string_piece.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/string_piece.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/tag.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/tag.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/token_type.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/tokenizer.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/tokenizer.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/tokenizer.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/tokenizer_states.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/utf8.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/utf8.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/utf8.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/util.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/util.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/util.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/vector.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/vector.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/vector.o
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/attribute.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/attribute.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/char_ref.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/char_ref.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/char_ref.rl
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/error.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/error.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/gumbo.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/insertion_mode.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/parser.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/parser.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/string_buffer.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/string_buffer.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/string_piece.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/string_piece.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/tag.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/token_type.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/tokenizer.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/tokenizer.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/tokenizer_states.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/utf8.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/utf8.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/util.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/util.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/vector.c
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/src/vector.h
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/lib/nokogumbo.rb
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/test-nokogumbo.rb
/usr/lib64/ruby/gems/2.2.0/specifications/nokogumbo-1.4.2.gemspec

%files dev
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/gumbo-parser/visualc/include/strings.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/nokogumbo-1.4.2/nokogumboc.so
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/ext/nokogumboc/nokogumboc.so
/usr/lib64/ruby/gems/2.2.0/gems/nokogumbo-1.4.2/lib/nokogumboc.so
